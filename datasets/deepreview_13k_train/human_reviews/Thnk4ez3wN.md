# On Learning Representations for Tabular Dataset Distillation

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Dataset distillation generates a small set of information-rich instances from a large dataset, resulting in reduced storage requirements, privacy or copyright risks, and computational costs for downstream modeling, though much of the research has focused on the image data modality. We study tabular data distillation, which brings in novel challenges such as the inherent feature heterogeneity and the common use of non-differentiable learning models (such as decision tree ensembles and nearest-neighbor predictors). To mitigate these challenges, we present TDColER, a tabular data distillation framework via column embeddings-based representation learning. To evaluate this framework, we also present a tabular data distillation benchmark, TDBench. Based on an elaborate evaluation on TDBench, resulting in 226,200 distilled datasets and 541,980 models trained on them, we demonstrate that TDColER is able to boost the distilled data quality of off-the-shelf distillation schemes by 0.5-143% across 7 different tabular learning models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a data distillation approach dedicated to tabular data. It uses the column representation to guide tabular data distillation. Specifically, this work first trains an encode to transform the original data to an intermediate representation for each column, then trains a decoder to recover the original data based on the intermediate representations. The distillation goal is to minimize the difference of intermediate column representation between the original and distilled tabular data. The comprehensive empirical results demonstrate the effectiveness of the proposed approaches.

### Strengths
1. This work investigate a important but less explored data modality, i.e., tabular data, in AI applications.
2. This work conduct a comprehensive assessment on 226,200 distilled dataset and 541,980 models trained on it.
3. The paper is easy to follow.

### Weaknesses
1. Although this paper conducts numerous experiments, the evaluation is based on a custom metric, relative regret, rather than on common metrics such as accuracy or mean squared error. This makes it difficult to compare the results with existing literature and understand the absolute performance of the proposed method. The use of a relative metric, while potentially useful for comparing across datasets, obscures the actual performance gains or losses achieved by the distillation process in terms of standard metrics.

2. I think it is valuable to consider whether the distillation process impacts inter-column correlations, which are crucial for downstream tasks in tabular data, such as data analysis. Specifically, an ablation study could investigate if the distillation process preserves or reduces the correlation between columns, potentially affecting the dataset’s utility for the downstream applications. It's important to quantify the extent to which the distilled data retains the original relationships between features, as these correlations often carry significant information.

3. It would strengthen this work if the authors could include a security and privacy analysis of their proposed TDColER. I am also curious whether the distilled dataset might introduce biases or vulnerabilities to adversarial attacks or privacy leakage. The paper should explore the potential for the distilled data to be more susceptible to membership inference attacks or to amplify existing biases in the original dataset.

4. The baseline comparison does not seem comprehensive. A comparison with other data distillation-like techniques, such as coreset selection [1], is missing.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the problem of tubular data distillation, and provides a comprehensive benchmark for existing models and datasets.

### Strengths
1. Tabular dataset distillation is an important and interesting problem.
2. The paper evaluates a large number of datasets, methods and different model architectures, and provides valuable insights.
3. The paper is well-written and easy to follow.

### Weaknesses
1. Limited Novelty.  While the paper addresses an important issue, the proposed framework includes column embedding based representation learning and a distillation function, both appear standard and pre-existing.  Combing them together appears a bit straightforward as well.   In addition, [1] also proposes an algorithm which project dataset into a latent space for data distillation. It is suggested that the paper discuss in-depth the novelty by comparing with recent works such as [1].

2. In Section 2, the paper points out two main characteristics for tabular data, but it is unclear how the proposed framework addresses these challenges. 

3. All the distillation methods considered are proposed before 2022. The paper also only compares its framework with the off-the-shelf distillation method. The authors should add more recent distillation methods (2022-2024), and compare with more recent baselines, such as [1] and baselines in Table 1 of [1] . 

Given the above concerns,  the authors may consider re-position the paper as a benchmark paper.

### Questions
how the proposed framework addresses the challenges unique for tabular data, exactly? That is, which part of the design is specifically applicable for tabular data?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the dataset distillation for tabular data and proposes a tabular data distillation framework TDColER via column embeddings-based representation learning.  Furthermore, a tabular data distillation benchmark, TDBench, is constructed to evaluate this framework.

### Strengths
1. Good Novelty: The research topic is interesting. It is essential to investigate the dataset distillation technique for real-world applications.

2. Comprehensive Evaluation: The authors conduct a comprehensive evaluation of the framework on a diverse set of 23 datasets from OpenML with many schemes and classifiers. 

3. Clear Presentation: The paper is well-organized and presents the proposed method and experimental results in a clear and concise manner.

### Weaknesses
1. While the paper mentions related work in the field of dataset distillation, it does not provide a detailed comparison with existing methods specifically designed for tabular data. I wonder whether the distilled dataset can improve the state-of-the-art methods.

2. The paper briefly mentions the use of column embeddings but does not provide a detailed explanation of how these embeddings are learned or their importance in the overall distillation process. This limits the understanding of the proposed method and its underlying mechanisms.

3. My biggest concern lies in the real-world task scenarios where models are trained solely on tabular data. As I understand, current research focuses on table-image multimodal data, utilizing tabular information to enhance models' image classification capabilities. The practical application of using tabular data alone seems unsuitable for dataset distillation, as tabular data are generally sensitive. Furthermore, tabular data occupy minimal storage space, raising the question of whether it is necessary to investigate dataset distillation for tabular data.

### Questions
Please refer to Weakness 3.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces TDColER, a novel framework designed for distilling tabular data. It addresses the challenges of feature heterogeneity and non-differentiable models commonly used with tabular data. The authors propose using column embeddings and representation learning to enhance the quality of distilled data. The paper also introduces TDBench, a benchmark for evaluating distillation methods on tabular data. Through extensive experiments, the authors demonstrate TDColER's ability to significantly improve the quality of distilled datasets across various models and datasets.

### Strengths
1. The paper introduces TDColER, a tabular data distillation method that effectively addresses key challenges in this field, such as inherent feature heterogeneity and the common use of non-differentiable learning models.
2. The authors construct TDBench, a tabular data distillation benchmark that includes a variety of distilled datasets and models, providing valuable resources for the research community.

### Weaknesses
 1. The main motivation for conducting tabular dataset distillation is not adequately articulated. The authors should clarify the importance of this area and the specific challenges they aim to address with their approach. A clear rationale for the need for tabular dataset distillation would significantly strengthen the paper's foundation.
 2. The paper occasionally lacks clarity in explaining key terms and concepts. For instance, on page 3, the authors mention "feature heterogeneity" and "non-differentiable learning models" without providing clear definitions. This lack of clarity may hinder the readability and accessibility of the research for readers unfamiliar with the nuances of tabular data processing. 
 3. The experimental section does not sufficiently demonstrate the superiority of TDColER compared to existing SOTA methods such as RDED and DATM. 
 4. The experimental section fails to provide a comparative analysis that highlights TDColER's efficiency and scalability relative to existing methods, such as the algorithm's complexity, resource consumption, and performance on larger dataset scales.
 5. The paper does not establish a theoretical foundation to explain the effectiveness of TDColER, particularly in terms of how it addresses feature heterogeneity and non-differentiable models.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2
