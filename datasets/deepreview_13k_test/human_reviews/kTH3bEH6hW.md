# Range-limited Augmentation for Few-shot Learning in Tabular Data

- Decision: Reject
- Scores: 6, 3, 5, 5

## Abstract
Few-shot learning is essential in many applications, particularly in tabular domains where the high cost of labeling often limits the availability of annotated data. To address this challenge, we propose range-limited augmentation for contrastive learning in tabular domains. Our augmentation method shuffles or samples values within predefined feature-specific ranges, preserving semantic consistency during contrastive learning to enhance few-shot classification performance. To evaluate the effectiveness of our approach, we introduce FeSTa (Few-Shot Tabular classification benchmark), a benchmark consisting of 42 tabular datasets and 31 algorithms. On this benchmark, contrastive learning with our augmentation method effectively preserves task-relevant information and significantly outperforms existing approaches, including supervised, unsupervised, self-supervised, semi-supervised, and foundation models. In particular, our method achieves an average rank of 2.3 out of 31 algorithms in the 1-shot learning scenario, demonstrating its robustness and effectiveness when labeled data is highly limited. The benchmark code is available in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel data augmentation method called Range-Limited Augmentation, which is designed to improve few-shot learning for tabular data. The proposed approach involves shuffling or sampling feature values within predefined ranges to maintain semantic consistency and improve model performance. Also, the paper introduces a Few-Shot Tabular Classification Benchmark (FESTA), encompassing 42 tabular datasets and 31 algorithms to evaluate the effectiveness of their approach. The paper demonstrates that the proposed method achieves superior results in one-shot classification scenarios, outperforming existing supervised, unsupervised, and foundation models.

### Strengths
1. The proposed range-limited augmentation is a unique solution to the challenge of maintaining semantic consistency in tabular data augmentations, which is crucial for effective contrastive learning.
2. The proposed FESTA benchmark offers a large-scale, diverse set of tabular datasets and learning paradigms, making it a valuable for future research opening.
3. The method shows substantial performance improvements, especially in 1-shot scenarios, and maintains competitive performance in 5-shot setups.
4. The analysis using mutual information and representation invariance score seems a reasonable choice to evaluate the quality of data augmentation.

### Weaknesses
1. The proposed method seems straightforward when applying to numerical features, but it is unclear how it can be adapted to categorical data. Also, it is not clearly analyzed how the proposed method perform in homogeneous tabular dataset.
2. The proposed method is evaluated only on proposed FESTA benchmark, which may not cover the entire trend in tabular data learning. For example, the paper could include OpenML-CC18 dataset as preliminary benchmark.
3. The proposed method only considers classification task, where regression tasks are also important aspect of tabular data learning.

### Questions
1. Could the author elaborate how the proposed range limited shuffling and range limited sampling applies to categorical features? 
2. Could the author provide empirical results on other popular OpenML dataset?
3. Could the proposed method be applied to regression tasks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposed two things. First, the few-shot learning benchmark for tabular datasets with a focus on 1 and 5-shot learning. Second, they proposed a data augmentation method for tabular datasets by additionally considering the range of the feature value for the feature augmentation. The author shows that the proposed method is effective by combining it with contrastive learning.

### Strengths
1. The overall paper is well-written and easy to read.

2. The author has conducted a new benchmark.

### Weaknesses
1. The proposed method is only applicable to numerical values. This is a highly critical weakness since many tabular datasets consist of categorical values.

2. Limited novelty. The proposed idea is a data augmentation method with a range limitation. In this regard, the only novelty is the range limitation, which I think is sensible as an engineering technique yet not as novel as an academic paper to be accepted.

3. The focused problem is too narrow. I do believe few-shot learning for tabular datasets [1] is important, but the more important problem is the full-shot setup. I think in a full-shot setup, the most dominant methods are tree-based methods, where the proposed method is somewhat hard to utilize. Furthermore, I think the author should consider a broader range of few-shot if they want to focus on few-shot learning, e.g., 8, 16, 32, and 64-shot learning.

4. In a few-shot tabular learning setup, recent LLM-based methods have become effective. I think it would be interesting to combine the current method with the LLM-based, few-shot, tabular learning methods [2,3,4,5].

5. It would be more interesting to suggest a new self-supervised learning (or any learning) method that can better leverage the proposed augmentation. I believe this will enhance the novelty.

In summary, I recommend rejection. The weakness mentioned above is quite critical and needs to be addressed. 

Reference\
[1] STUNT: Few-shot Tabular Learning with Self-generated Tasks from Unlabeled Tables, ICLR 2023\
[2] LIFT: Language-Interfaced Fine-Tuning for Non-Language Machine Learning Tasks, NeurIPS 2022\
[3] Language models are weak learners, NeurIPS 2023\
[4] Large Language Models Can Automatically Engineer Features for Few-Shot Tabular Learning, ICML 2024\
[5] Tabular Transfer Learning via Prompting LLMs, COLM 2024

### Questions
Please refer to the weakness part above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses a challenge in tabular data with approaches from few-shot learning. In particular, this paper proposes range-limited augmentation equipped with contrastive learning to build a model capable of tackling learning on tabular domains. The proposed approach provides augmentation by shuffling or sampling values within predefined feature-specific ranges, preserving semantic consistency. In addition to the proposed approach, this paper also introduces a benchmark to evaluate the efficacy of  the proposed approach compared to the counterparts so-called Few-Shot Tabular Classification (FESTA). Through experiments on the benchmark, the proposed approach with augmentation with contrastive learning the performance can be improved compared to the state-of-the-arts in few-shot learning.

### Strengths
- This paper introduces an underexplored problem by focusing few-shot learning on tabular data. This is due to data unavailability in tabular domains, prohibiting training in a large scale manner. Thus, few-shot learning is a reasonable perspective in tackling such problems.
- This work also introduces a novel benchmark with 42 tabular datasets and 31 techniques for comparison. This benchmark has the potential to serve as a resource for future research efforts, providing a standardized comparison and facilitating the evaluation of new methods in tabular data analysis.

### Weaknesses
- The problem scope is quite narrow and the proposed approach only works well in tabular domains. Additionally, the proposed augmentation approach demonstrates effectiveness primarily within tabular data domains and might not generalize to other types of data structures or formats.
- This paper has serious clarity issues in terms of problem introduction. The problem in this work is not elaborated well in the paper. The problem setup is quite general in which previous few-shot learning papers have discussed it. However, a specific focus problem setup on tabular domains is not described in the paper. Additionally, there is no clear problem description to differentiate among few-shot learning in several domains e.g., image, text, and tabular domains. This causes confusion in understanding the core problem in tabular domains compared to other modalities.
- Based on my understanding, the augmentation method is based on the ranged limited shuffling and sampling. However, this method is largely inspired by augmentation methods in the image domain, but here it is applied to a different domain. The strategy closely resembles what SimCLR introduced in its paper, with only a specific range constraint added to the technique. In SimCLR, we can interpret “range-limited sampling” as modifying the colors from a range between 0-255, and shuffling as cropping from a specific region. Therefore, the novelty of this approach sounds quite limited.
- The writing is quite poor. There are many irrelevant points in the paper e.g., lists of detailed baselines and augmentation. These sections do not provide meaningful insights or support the main contributions. As a result, the core contributions are obscured by unrelated information that does not directly connect to the main focus of the paper.

### Questions
This paper missed explanation on how each method can be used to the problem at hands. For instance, XGBoost, CatBoost, LightBGM are not methods designed for few-shot learning. How are these methods modified to accommodate learning with a few data?

### Soundness
2

### Presentation
2

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
This paper introduces the limited range expansion of a small amount of learning in tabular data. This method aims at maintaining semantic consistency in the learning process, which is very important to improve the classification performance under the condition of limited labeled data. The authors have proved the effectiveness of their method through a new benchmark test, which is superior to the existing methods.

### Strengths
Originality: The concept of range-limited augmentation for contrastive learning in tabular data is novel. The paper introduces a creative solution to the challenge of designing augmentations that preserve task-relevant information in a domain. The application of distribution-based range limiting to augmentation strategies is an innovative approach that leverages the inherent structure of tabular data, which is a creative combination of existing ideas in data augmentation and representation learning. The introduction of the FESTA benchmark is original as it addresses a gap in the evaluation of few-shot learning methods for tabular data, providing a new resource for the community.
Quality: The paper is well-structured, with a clear problem statement, detailed methodology, comprehensive experiments. The paper provides a rigorous evaluation of the proposed method through extensive experiments on a diverse set of datasets and algorithms.
Clarity: The paper is well-written, with a clear and logical flow that makes it easy to follow the authors' line of reasoning.
Significance: The paper addresses a significant problem in the field of machine learning, where labeled data is often scarce, especially in specialized domains like healthcare or finance. The proposed solution has the potential to impact a wide range of applications by enabling more effective learning from limited labeled data, which is a common scenario in many real-world scenarios. It provides a standardized way to evaluate and compare few-shot learning methods in tabular data, which could drive further research and development in this area.

### Weaknesses
1. The paper provides empirical evidence of the effectiveness of the proposed method but does not offer a theoretical analysis of why range-limited augmentation works better than other methods in preserving task-relevant information.  Developing a theoretical framework to explain these observations could further strengthen the contribution.
2. In classifiation-related papers, confusion matrix is an important basis for judging a classifier, so it is suggested to add more blanks here.
3. There are some typos in the manuscripts. The presentation of this manuscript can be improved.

### Questions
1. Can you provide a theoretical explanation for how effective a scope-limited augmentation method is in preserving task-related information compared to other augmentation methods?
2. What specific optimizations can be implemented to reduce the computational overhead associated with scope-constrained enrichment?
3. Will the benchmark code be exposed on a platform like GitHub to promote reproducibility?
4. Based on the findings of this study, what are the plans for future research?

### Soundness
3

### Presentation
3

### Contribution
3
