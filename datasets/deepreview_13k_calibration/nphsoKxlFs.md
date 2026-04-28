# Dynamic Contrastive Learning for Time Series Representation

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Understanding events in time series is an important task in a variety of contexts. However, human analysis and labeling are expensive and time-consuming. Therefore, it is advantageous to learn embeddings for moments in time series in an \textit{unsupervised} way, which allows for good performance in classification or detection tasks after later minimal human labeling. In this paper, we propose \textit{dynamic contrastive learning} (DynaCL), an unsupervised contrastive representation learning framework for time series that uses temporal adjacent steps to define positive pairs. DynaCL adopts N-pair loss to dynamically treat all samples in a batch as positive or negative pairs, enabling efficient training and addressing the challenges of complicated sampling of positives. We demonstrate that DynaCL embeds instances from time series into semantically meaningful clusters, which allows superior performance on downstream tasks on a variety of public time series datasets. Our findings also reveal that high scores on unsupervised clustering metrics do not guarantee that the representations are useful in downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces DynaCL, a novel framework for learning time series representations in an unsupervised manner by leveraging adjacent time steps as positive pairs, thus simplifying the learning process without complex augmentations. Using an MP-Xent loss function, DynaCL effectively captures temporal patterns, enabling high-quality embeddings. An extended version, DynaCL-M, incorporates feature prediction and dynamic margins to enhance clustering, though this sometimes sacrifices downstream task performance. Tested on multiple datasets, DynaCL achieves competitive results in classification and clustering, demonstrating efficient training and a practical approach for time series data representation.

### Strengths
1. This paper provides an insightful analysis by contrasting clustering scores (like Davies-Bouldin Index and Silhouette Score) with downstream task performance. This comparison reveals that high clustering metrics do not always equate to useful representations in practical tasks, highlighting the limitations of relying solely on clustering for evaluating representation quality.

2. The introduction of a margin in DynaCL-M is a valuable addition. It allows the model to adjust the separation between positive and negative pairs adaptively based on their temporal proximity, enhancing the flexibility and performance of the learned representations, especially in complex time series where adjacent steps may differ.

### Weaknesses
1. **Lack of Novelty in MP-Xent**: The MP-Xent loss function in this paper closely resembles existing approaches like Soft-Nearest Neighbors (SoftCLT), which also leverages multiple positive pairs within a batch. In particular, MP-Xent appears quite similar to soft temporal contrastive learning. This similarity raises questions about the novelty of the loss function, as MP-Xent seems more like an adaptation of established methods than an entirely new approach. Furthermore, MP-Xent can be seen as a specific variant of soft temporal contrastive learning, focused exclusively on temporally adjacent samples, which may limit its generalizability to broader instance-wise contrastive learning contexts.

2. **Limited Datasets in Experimental Evaluation**: The paper’s experiments are limited to just three datasets, which restricts the generalizability of its findings. For a more robust evaluation, the model should be tested on a wider range of datasets, such as the 125 UCR and 29 UEA benchmarks commonly used in time series classification. Additionally, while there is an extensive description of the datasets used, more impactful would be to include semi-supervised and transfer learning experiments, as these are standard benchmarks in time series representation learning and would better demonstrate the model’s versatility across diverse applications.

3. **Missing Important Baselines**: Some key baselines are missing in the comparison, specifically SoftCLT, which has significant conceptual overlap with MP-Xent, and TimeDRL, which also tackles positive pair selection without explicit augmentations (using dropout instead). Excluding them from the experiments limits the comprehensiveness of the baseline comparisons, leaving the results less conclusive than they might otherwise be.

### Questions
1. In formula (3), it is evident that both instance-wise and temporal contrastive learning are considered. However, the paper predominantly emphasizes temporal contrastive learning throughout, which creates some confusion. In contrast, SoftCLT clearly differentiates between instance-wise and temporal contrastive learning. Furthermore, does the “multiple positive pairs” mechanism only apply to temporal contrastive learning? If I’m mistaken, please clarify, but it seems this mechanism is not applied to instance-wise contrastive learning. To enhance clarity, it would be beneficial if the authors could further elaborate on their approach to instance-wise versus temporal contrastive learning and how it compares to SoftCLT's handling of these two forms of contrast. This clarification could help address the potential confusion and provide readers with a clearer understanding of the framework's scope and application.
2. In Section 4.5, do all self-supervised learning models use the same backbone architecture? It would be more fair and consistent to use the same backbone encoder across all models for accurate comparison.

### Soundness
3

### Presentation
3

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
This paper introduces Dynamic Contrastive Learning (DynaCL), an unsupervised method for embedding time series data to improve performance in subsequent classification and detection tasks with minimal human intervention. DynaCL defines positive pairs based on temporal adjacency, utilizing N-pair loss to dynamically adjust sample pairings during training. By doing so, it efficiently learns representations that form semantically meaningful clusters, achieving strong performance on various public time series datasets. The study highlights that high unsupervised clustering metrics do not necessarily translate to improved performance in downstream tasks, emphasizing the need for careful consideration of representation quality beyond clustering alone.

### Strengths
1. The methodology is clear and the problem is well-motivated.
2. The proposed method has fairly good novelty.
3. The experiments for different setups are detailed.

### Weaknesses
1. The author needs to compare against recent works on SOTA time series contrastive learning frameworks like InfoMin, SoftCLT, etc. 
2. The author could consider other time-series domains like UCIHAR, UEA, and UCR datasets to evaluate against.

### Questions
1. How does the proposed time series representation method perform on sequential tasks, such as the commonly used prediction task?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors present  Dynamic Contrastive Learning (DynaCL), a new approach for unsupervised representation learning in time series analysis. DynaCL employs contrastive learning by pairing adjacent time steps as positives, leveraging an N-pair loss strategy to treat all samples within a batch as potential positive or negative pairs. Experimental results demonstrate that DynaCL embeds instances from time series into semantically meaningful clusters, allowing superior performance on downstream tasks on various public time series datasets.

### Strengths
1. The authors compare **DynaCL** against state-of-the-art baselines for time series representation learning on clustering quality and event classification, these are uncommon but meaningful in the time series representation domain.
2.  The notation used by the authors in the paper is relatively consistent and clear.
3. The authors' experiments are relatively comprehensive.

### Weaknesses
Generally, the technique of the manuscript is partially sound, however, the novelty is marginal and some major concerns are listed below:
1. There is a significant logical issue in this paper: the authors claim that the main focus of contrastive learning for time series lies in the construction of positive and negative sample pairs. However, contrastive learning generally involves three key components: constructing positive and negative pairs, designing an encoder to map the original data to a hidden space, and formulating the contrastive loss function [1]. Thus, the authors do not necessarily find the most critical step but rather assert that sample pair construction is the most important. Furthermore, it is evident throughout the paper that the design or selection of the contrastive loss function is also essential, especially in the related work section. This weakens the clarity of the paper’s motivation.
2. The authors aim to convey that "understanding events in time series is an important task in various contexts." However, the paper's self-supervised learning approach focuses on moments, and it lacks an adequate explanation to help readers understand how modeling moments contributes to understanding events. Additionally, the authors need some references in the opening sentence of the introduction on line 28 to support the prevalence of event labeling.
3. The authors claim that “Currently, TS representation learning that leverages temporal information in the contrastive objective relies on complicated statistical approaches for sampling positives”. However, there are many existing methods for constructing positive and negative sample pairs, not limited to complex statistical approaches. The references cited by the authors are not very up-to-date, with the most recent being IJCAI 2023.
4. The innovation of this paper is modest, as the emphasized addition of positive samples can be viewed as a special case of [2].

### Questions
Please answer the following questions combined with the content in weakness.

Why does DynaCL-M still fail to perform consistently well across the two downstream tasks, even after adding two augmentations to DynaCL?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a dynamic contrastive learning method for time series representation learning, which harness every time step in a sequence as positive and negative pairs. Experiments are carried out on clustering and classification tasks.

### Strengths
1. The motivation of introducing SSL for time series modeling is clear.
1. The paper is well-structed.

### Weaknesses
1. Related works are not sucfficient. More relevant studies should be discussed, e.g., soft contrastive learning for time series (ICLR 2024), Towards Enhancing Time Series Contrastive Learning: A Dynamic Bad Pair Mining Approach (ICLR 2024)

2. Continue with 1, the contribution and novelty of the proposed approach is unclear. As there are numuous methods that leverage contrastive learning for time series, what is the specific innovations of the proposed approach in comparison with them? I have not seen new insights and new techniques.

3. The experiments are weak. On the one hand, recent advanced baselines, e.g., SimMTM, and those menthoned in #1, are missed. On the other hand, more datasets (e.g., UCR classification datasets) and tasks (e.g., forecasting) should be evaluated.

### Questions
Please address the weakness.

### Soundness
1

### Presentation
2

### Contribution
1
