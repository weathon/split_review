# Spatio-Temporal Graph Knowledge Distillation

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Large-scale spatio-temporal prediction is a critical area of research in data-driven urban computing, with far-reaching implications for transportation, public safety, and environmental monitoring. However, the challenges of scalability and generalization continue to pose significant obstacles. While many advanced models rely on Graph Neural Networks (GNNs) to encode spatial and temporal correlations, they often struggle with the increased time and space complexity of large-scale datasets. The recursive GNN-based message passing schemes used in these models can make their training and deployment difficult in real-life urban sensing scenarios. Additionally, large-scale spatio-temporal data spanning long time spans introduce distribution shifts, further highlighting the need for models with improved generalization performance. To address these challenges, we propose Spatio-Temporal Graph Knowledge Distillation (STGKD) paradigm to learn lightweight and robust Multi-Layer Perceptrons (MLPs) through effective knowledge distillation from cumbersome spatio-temporal GNNs. To ensure robust knowledge distillation, we integrate the spatio-temporal information bottleneck with the teacher-bounded regression loss. This allows us to filter out task-irrelevant noise and avoid erroneous guidance, resulting in robust knowledge transfer. Additionally, we enhance the generalization ability of student MLP by incorporating spatial and temporal prompts to inject downstream task contexts. We evaluate our framework on three large-scale spatio-temporal datasets for various urban computing tasks. Experimental results demonstrate that our model outperforms state-of-the-art approaches in terms of both efficiency and accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces the Spatio-Temporal Graph Knowledge Distillation (STGKD) framework, designed to tackle the scalability and generalization challenges in large-scale spatio-temporal prediction for urban computing applications like transportation, public safety, and environmental monitoring. While Graph Neural Networks (GNNs) are commonly used for capturing spatial-temporal correlations, they struggle with large-scale datasets and changing data distributions over time. STGKD addresses these issues by transferring knowledge from complex GNNs to more efficient Multi-Layer Perceptrons (MLPs), improving scalability and efficiency. This is achieved through a robust knowledge distillation process, integrating a spatio-temporal information bottleneck and a teacher-bounded regression loss to filter out noise and prevent erroneous guidance. Additionally, spatial and temporal prompts are incorporated to enhance the generalization capability of the student MLP, helping it to adapt to distribution shifts and unseen data. The proposed paradigm is evaluated on three large-scale spatio-temporal datasets, demonstrating superior performance in terms of efficiency and accuracy compared to state-of-the-art models. The implementation of STGKD is made available for reproducibility, showcasing its practical applicability and effectiveness in urban computing domains.

### Strengths
The authors have provided an extensive and meticulous set of experiments, encompassing various studies like ablation, scalability, generalization, and robustness, ensuring a thorough evaluation of their work.

The methodology introduced in the paper offers a fresh perspective, utilizing both spatial and temporal prompts to unravel dynamic patterns, which presents an intriguing approach.

The paper articulates a well-defined research question, and the data is effectively communicated through well-structured figures and tables.

### Weaknesses
Clarity in the Introduction:
The flow of logic in the introductory section needs to be refined. The paper initially highlights that most existing research prioritizes spatial dependency, followed by a discussion on the challenges of generalization and scalability. However, these sections seem disjointed. Furthermore, introducing the paper's contributions prior to addressing challenges like noise does not establish a coherent narrative.
Lack of Motivation:
It is crucial to elucidate the motivation behind the proposed approach in the introduction to provide readers with a clear understanding of its relevance and significance.
Preliminary Section Gaps:
The preliminary section covers two prevalent concepts, yet it falls short by not including knowledge distillation. This addition is necessary for a comprehensive understanding of the topic.
Ambiguity in Approach Explanation:
The description of the approach leaves room for improvement. For instance, the statement, "Our goal is to distill the valuable knowledge embedded in the GNN teacher and effectively transfer it to a simpler MLP, enabling more efficient and streamlined learning," raises questions about what constitutes 'valuable knowledge' and why this process makes the MLP more efficient rather than more effective. Specifically, it is unclear how the distilled knowledge leads to efficiency gains in the MLP, as opposed to simply improving its predictive performance. The nature of this 'valuable knowledge' and the mechanism by which it enhances efficiency needs to be more clearly defined. Also, the term 'prompt' is used without sufficient explanation. It is unclear if these prompts are learnable parameters, contextual features derived from the input data, or something else entirely. The paper needs to clarify the nature of these prompts and how they are integrated into the model.
In terms of novelty and motivation, the manuscript does not make a strong case. While it appears that the authors might be introducing knowledge distillation to the GNN domain for the first time (though this is not explicitly claimed in the paper), this alone does not constitute a substantial contribution. The paper needs to delineate the differences between traditional knowledge distillation approaches applied to CNNs and STGNNs, and the proposed method, explaining why it is particularly effective in the GNN context. The specific challenges of applying knowledge distillation to spatio-temporal data, compared to image data, are not clearly articulated. It is also not clear why the proposed method is superior to existing knowledge distillation methods when applied to STGNNs.

### Questions
1. What are the significant differences between applying the knowledge distillation to CNN and STGNN?
2. For SPATIO-TEMPORAL IB INSTANTIATING, what is the spatio-temporal part here?
3. The paper uses the term prompt. What is the difference between the prompt you used and spatio-temporal features? Could I regard it as contextual spatio-temporal features?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors leverage the concept of knowledge distillation within graph structures to address the challenges of generalization and scalability in spatio-temporal graph forecasting. Their innovative approach involves compressing expansive GNNs into more compact and efficient MLPs. This compression is achieved through the Spatio-Temporal Graph Knowledge Distillation paradigm, which ensures robust knowledge transfer by filtering out task-irrelevant noise using an integrated spatio-temporal information bottleneck. Furthermore, by adopting the teacher-bounded regression loss, the model avoids misguided directions during the learning process. The added spatio-temporal prompts provide the student MLP with richer context from downstream tasks, further enhancing its generalization capabilities. After spatio-temporal datasets, the results confirm the framework's superiority, outclassing existing models in both efficiency and accuracy.

### Strengths
(1) The paper's presentation is top-notch. Its use of plots, clear definitions, and intuitive explanations significantly enhance the reader's understanding.

(2) The motivation driving the research question is cogently articulated.

(3)  The authors showcased the breadth of their research by selecting a diverse range of datasets. Their comprehensive ablation study, encompassing Spatio-Temporal Prompt Learning, Spatio-Temporal IB, Teacher-Bounded Regression Loss, and Spatio-Temporal Knowledge Distillation, is commendable. I appreciate their meticulous approach in Section 4 to test scalability, generalization, and robustness, aligning perfectly with the research's core motivation.

### Weaknesses
 (1) Novelty: My primary concern pertains to the paper's novelty. While the authors posit that the integration of the spatio-temporal information bottleneck into the Knowledge Distillation (KD) framework is a significant contribution, I'd like to highlight that the concept of the information bottleneck has already been explored in the context of knowledge distillation[1]. Moreover, the idea of employing knowledge distillation on dynamic graphs isn't novel either[2,3,4]. It appears the authors are leveraging well-established ideas to tackle specific challenges in spatial-temporal graph forecasting.

(2) Evaluation: Another area of improvement is in the choice of baseline models for evaluation. Notably, the absence of other graph knowledge distillation models as baselines seems to be an oversight. Including them would make the comparison more comprehensive and equitable.

### Questions
(1) Could the authors clarify the distinct contributions that set their approach apart from existing methods in graph knowledge distillation?

(2) For a comprehensive evaluation, why were other graph knowledge distillation models not considered as baseline models? Would incorporating them not offer a more balanced and insightful comparison in the context of your study?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores a critical area of research in large-scale spatio-temporal prediction. The poor scalability and generalizability of existing spatio-temporal model hinder their deployment in real-world urban scenarios. To this end, the authors propose Spatio-Temporal Graph Knowledge Distillation (STGKD) paradigm to learn lightweight and robust MLPs through effective knowledge distillation from cumbersome spatio-temporal GNNs. Robust knowledge distillation is achieved by integrating the spatio-temporal information bottleneck with the teacher-bounded regression loss. To further enhance the generalizability of student MLP, the authors incorporate learnable spatial and temporal prompts into the student model's input so as to inject downstream task contexts. Experimental results show that the proposed model outperforms state-of-the-art approaches in terms of both efficiency and accuracy.

### Strengths
1. The paper is well-motivated. The study of large-scale spatiotemporal prediction models has wide-ranging potential applications, and the issue of spatiotemporal distribution shift is indeed a crucial challenge that needs to be addressed for achieving accurate predictions in long-term and large-scale scenarios.

2. The authors have provided a clear and coherent explanation of the motivation behind the design of various modules of the STGKD model. 

3. The logical structure of the paper is well-organized and easy to follow.

4. The experimental results presented in the paper are comprehensive and well-designed, covering overall performances, ablation studies, and case studies.

### Weaknesses
 1. The analysis of challenges in the introduction section is rather general and does not elaborate on the unique challenges in addressing the issues of scalability and generalization in designing methods for spatiotemporal scenarios.

 2. As stated in the related works, 'A significant contribution of this work lies in the novel integration of the spatio-temporal information bottleneck into the KD framework.' However, it should be noted that the incorporation of the information bottleneck into knowledge distillation has been previously explored, e.g., see references [3] [4] below. The paper lacks clarification on how the proposed method differs from existing approaches.

 3. As an ICLR submission, the paper lacks theoretical guarantees. For instance, it is better to quantify the model's robustness against noise after adopting such information bottleneck regularizer. Additionally, as reducing complexity of the model is an important idea of knowledge distillation, providing a generalization bound related to the model's complexity would strengthen the method's support.

 4. Regarding spatio-temporal prompt learning module, here are two weaknesses:

   (a) A comparison with existing prompt learning methods is missing, and the similarities and differences should be clarified to prevent confusion.

   (b) Utilizing three types of prompts as input and a learnable embedding method has been done in previous STGNN works [1,2], limiting the novelty of the proposed method.

 5. Weaknesses in experiments:

   (a) The overall performance improvements of the proposed model on all datasets are not significant.

   (b) The STID model, which is similar to the proposed model but without the knowledge distillation module, outperforms most complex STGNNs, raising the question of why transferring knowledge from weaker STGNNs to MLPs can lead to improvement. However, the paper does not offer clear explanations for this phenomenon.

   (c) To achieve a fair comparison, the model-agnostic spatio-temporal prompt learning should be incorporated into SOTA STGNNs

   (d) The authors have conducted generalizability testing on PEMS data with synthesized data missing. However, this type of distribution is only one specific example of covariate shift, and there are various other types of distribution shifts that need to be considered, e.g., the distribution shifts of traffic patterns during rush hours or seasonal traffic patterns shifts.

### Questions
see weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new framework called STGKD for spatio-temporal graph knowledge distillation, which aims to encode robust and generalizable representations of spatio-temporal graphs. The framework incorporates the IB principle to enhance the knowledge distillation process by filtering out task-irrelevant noise in the student’s encoding and alignment during knowledge transfer. Moreover, it introduces a spatio-temporal prompt learning component that injects dynamic context from the downstream prediction task. Through extensive experiments, the authors demonstrate that STGKD surpasses state-of-the-art models in both performance and efficiency. The paper's contributions include addressing the challenges of efficiency and generalization in large-scale spatio-temporal prediction, introducing a novel and versatile framework, and demonstrating the effectiveness of the proposed approach through extensive experiments.

### Strengths
S1. In terms of originality, the paper presents a new paradigm for learning lightweight and robust Multi-Layer Perceptrons through effective knowledge distillation from cumbersome spatio-temporal Graph Neural Networks. The incorporation of the IB principle and spatio-temporal prompt learning components is also a novel contribution to the field.
S2. The quality of the paper is high, as the authors provide a clear and detailed description of the proposed framework, including the technical details and experimental methodology. The experiments are well-designed and conducted, with extensive evaluations on various spatio-temporal forecasting tasks. 
S3. The clarity of the paper is also commendable, as the authors provide a clear and concise introduction to the problem, a detailed description of the proposed framework, and a thorough evaluation of the results. The paper is well-organized and easy to follow, with clear and informative figures and tables.

### Weaknesses
W1. The dataset lacks a detailed description. Traffic Data and Crime Data lack links or citations to papers. It would also be good to have a table that describes the size of the dataset along with some other information that would give the reader a clearer picture of the dataset. In addition, there is a detail error, in Datasets the serial number in front of Weather Data should be iii) instead of ii).
W2. Limited discussion of the limitations and potential problems. The paper does not provide a detailed discussion of the limitations of the proposed framework or potential extensions to the work.
W3. The experiment lacks a comparison of runtime. In addition to the comparison of efficiency, the running time of the different methods should also be compared, which is also a very important indicator.

### Questions
Can authors provide a more detailed explanation of the interpretability and explainability of the proposed framework? The paper mentions that the student MLP selectively inherits task-relevant spatio-temporal knowledge from the teacher GNN framework , but it does not provide a clear explanation of how this knowledge transfer occurs and how the student model utilizes the transferred knowledge. Including a more detailed discussion on the interpretability and explainability of the framework would enhance the understanding of the proposed approach and its inner workings.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
