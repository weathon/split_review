# RoFt-Mol: Benchmarking Robust Fine-tuning with Molecular Graph Foundation Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
In the era of foundation models, fine-tuning pre-trained models for specific downstream tasks has become crucial. This drives the need for robust fine-tuning methods to address challenges such as model overfitting and sparse labeling. Molecular graph foundation models (MGFMs) face unique difficulties that complicate fine-tuning. These models are limited by smaller pre-training datasets and more severe data scarcity for downstream tasks, both of which require enhanced model generalization. Moreover, MGFMs must accommodate diverse pre-training objectives, including both regression and classification tasks. To better understand and improve fine-tuning techniques under these conditions, we classify eight fine-tuning methods into three mechanisms: weight-based fine-tuning, representation-based fine-tuning, and partial fine-tuning. We benchmark these methods on downstream regression and classification tasks across both supervised and self-supervised pre-trained models in diverse labeling settings. This extensive evaluation provides valuable insights and informs the design of a refined robust fine-tuning method, DWiSE-FT. This approach combines the strengths of simple post-hoc weight interpolation with more complex weight ensemble fine-tuning methods, delivering improved performance across both task types while maintaining the ease of use inherent in post-hoc weight interpolation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores optimal Fine Tuning (FT) strategies for molecular representation, addressing challenges such as label scarcity and distribution shifts. It introduces an enhanced FT method, DWiSE-FT, tailored for diverse pre-trained molecular graph models. This method promises efficiency and automation in specific FT scenarios, consistently achieving top-ranking results.

### Strengths
- I have found the paper well written and self-contained. I think a non-expert could find most of the information in the paper, and I appreciate this aspect.

 - Figure 1, which demonstrate the problem domain and architecture, are interesting and easy to read. I commend the authors for their explicit effort in making these illustrations clear and informative.

 - The insights are didactical and well communicated. The conclusion given by the experiments looks interesting and valuable for future practitioners, while I think a synthesis would be beneficial for the reader.

### Weaknesses
Despite these merits, I have the following concerns about the paper.

1- While there is a careful analysis of the different design decisions/performance tradeoffs, I feel that there is only a limited understanding about what are the properties of the Architecture that lead to these decisions/performance differences.


2-  The study's scope, while broad, does not extend to a multi-task, multi-modality approach that could significantly enhance its applicability and impact. It does not explore foundation models across diverse scientific domains such as RNA,  and proteins nor does it address varied scientific tasks likechemical reactions. Expanding the research to cover these aspects would substantially enrich the study's utility and relevance.

3- While the study incorporates several representative FineTuning (FT) methods from various categories, it does not investigate additional FT methods from other categories that could offer significant insights. I have mentioned some noteworthy models here that deserve further exploration:
“DPA-2: A Large Atomic Model as a Multi-Task Learner [Zhang 2023]”
“Scalable Training of Trustworthy and Energy-Efficient Predictive Graph Foundation Models for Atomistic Materials Modeling: A Case Study with HydraGNN [Pasini 2024]”
“MiniMol: A Parameter-Efficient Foundation Model for Molecular Learning [Klaser 2024]”

### Questions
is there any sensitivity analysis on key hyperparameters of DWiSE-FT? I would also suggest comparing the hyperparameter sensitivity of DWiSE-FT to that of baseline methods.

### Soundness
2

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
In this work, the authors proposed a novel benchmark to understand the impact of different fine-tuning methods for pre-trained molecular foundation models in downstream tasks. Specifically, 8 fine-tuning methods grouped in 3 categories are benchmarked over 12 datasets and 36 experimental settings. Insights are then derived from the experimental results to understand which methods are best suited for which needs. In addition, a refined method named DWiSE-FT is proposed to enable more efficient fine-tuning with competitive performance.

### Strengths
Recently, various foundation models for molecular graphs have been proposed, however, to apply them in downstream tasks, a well-designed fine-tuning procedure is required. This work benchmarks a wide range of fine-tuning methods to provide insight into this aspect. Here are the strengths of the work: 

- **Important direction.** Understanding how to select the best fine-tuning strategy for a downstream task is highly important for molecular foundation models. 

- **Extensive experiments.** In this work, 8 FT methods are examined and compared across 12 datasets and 36 experimental settings, providing an empirical comparison for a variety of settings. 

- **novel method DWiSE-FT.** The authors proposed DWiSE-FT which is a great candidate for regression datasets.

### Weaknesses
Here are the weaknesses of this work. 

- **lack of new datasets.** The main contribution of this work is proposing a novel benchmark for fine-tuning. However, there are no novel datasets to provide more benchmark environments outside of existing datasets. This limits the scope of the benchmark and its ability to generalize to unseen data distributions. The value of a benchmark is significantly increased when it can evaluate models on data not previously used in training or evaluation, which this work does not address.

- **over-simplified backbone.** The authors mention that "high model expressiveness" is needed to capture the semantics of molecular datasets. However, for experiments, only a 5-layer GIN architecture is used as the backbone, which is known to be limited by the 1-WL test in expressiveness. A more powerful architecture can be used such as GraphGPS[1] or Graphormer [2]. Experiments with a more powerful backbone PT architecture can also provide more insight into the impact of the choice of PT architecture. The choice of a GIN limits the conclusions that can be drawn about the effectiveness of the fine-tuning methods on more expressive architectures.

- **limited pre-training for Graphium.** In the Graphium paper, three categories of datasets are provided: Toymix, Largemix, and UltraLarge. It would be more interesting to observe results for PT models trained on Largemix or both Toymix and Largemix. The use of only the Toymix pre-trained model restricts the conclusions that can be made about the impact of pre-training data scale and diversity on downstream fine-tuning performance. Exploring the impact of different pre-training datasets would provide a more comprehensive benchmark.

### Questions
-  The tables in the paper are too small and very hard to read or draw conclusions from. For example, Table 3 is very small and not readable at all.  The authors should update the format of the Table or move less relevant content to the appendix. 

- I can't entire agree with the claim on line 47 "pre-trained on insufficient amount of PT data
(1M-100M samples) and vocabularies". The authors made several comparisons between the molecular foundation model and foundation models from NLP / vision throughout the paper. However, the reality is that molecular data is significantly harder to curate and needs to be explicitly constructed for effective learning. Thus, I don't believe that the same scale of available data for NLP or vision would ever be available for molecular learning. For example, 100 M molecular graphs are already a large number and the focus should instead be in more to design effective PT and FT strategies. If possible, the authors should revise this claim.

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
This paper presents a benchmarking study on robust fine-tuning (FT) with molecular graph foundation models. The authors evaluate different fine-tuning strategies under supervised and self-supervised pre-training (PT) paradigms, using various molecular datasets. They introduce a refined method called DWiSE-FT, which consolidates the strengths of existing FT methods and demonstrates improved efficiency while maintaining promising results for regression tasks.

### Strengths
1. Comprehensive Evaluation:The paper conducts an extensive evaluation of different fine-tuning strategies across multiple datasets, providing a comprehensive understanding of their performance.
2. The introduction of DWiSE-FT represents a novel approach to fine-tuning, combining the strengths of existing methods.
3. The paper provides valuable insights into the design of FT methodologies and practical guidance for molecular representation learning. The findings have implications for both researchers and practitioners working in the field of molecular graph representation learning.

### Weaknesses
1. While the paper compares different fine-tuning strategies, it does not provide a detailed comparison of DWiSE-FT with other state-of-the-art methods in the field. This paper presents a benchmarking study, the comparisons and findings are important and novel. I want to know the importance of this proposed method DWiSE-FT , can it be presented in a research paper?
2. The abbreviation PT in Line 15 has no explanations.
3. In sec 2.2, the authors present different fine-tuning methods, the proposed Adaptive post-hoc ensemble method is similar with WiSE-FT. More information about the computational efficiency and scalability of DWiSE-FT would be beneficial. 
4. Explore the performance of DWiSE-FT in combination with other pre-training paradigms.
5. The findings in this paper seems common, which is similar in other public datasets, could you provide more insights on MOLECULAR research?

### Questions
1. In Line111-115, why choose GraphMAE and Mole-BERT as the PT model?

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
This paper addresses the challenges and importance of fine-tuning pre-trained molecular graph models. The work explores 8 fine-tuning methods categorized into weight-based, representation-based, and partial FT, benchmarked across 12 datasets with 36 experimental settings. These settings aim to simulate real-world FT scenarios, including OOD generalization and Fewshot settings. The paper highlights the strengths of different FT strategies depending on whether tasks are classification or regression-based. A new method, DWiSE-FT, is proposed, combining aspects of weight-based methods to enhance fine-tuning efficiency.

### Strengths
1. The paper benchmarks 8 FT methods across 12 datasets and various experimental settings, providing a thorough evaluation of the fine-tuning methods for molecular graph models.

2. This paper proposes DWiSE-FT based on their findings, and DWiSE-FT performs well on regression tasks.

3. The benchmark is similar to the practical scenarios of molecular representation learning, by including scaffold and size splitting.

### Weaknesses
1. The pre-trained molecular models evaluated in this paper, such as Mole-BERT and Graph MAE are small in scale compared to other foundation models. The authors should evaluate more powerful pre-trained models such as [1] and [2].

2. Though DWiSE-FT shows improved performance, it is based on existing FT strategies rather than novel FT methods.

### Questions
1.  Recently, many multi-modal molecular graph models have been proposed. These models can gain additional information from texts and thus are more expressive. Can you conduct experiments on these more expressive molecular graph models such as [1] and [2]? 

2. How do scaffold and size splits, which simulate OOD challenges, impact the robustness of fine-tuning methods in molecular property prediction tasks?

[1] MolCA: Molecular Graph-Language Modeling with Cross-Modal Projector and Uni-Modal Adapter
[2] Multi-modal Molecule Structure-text Model for Text-based Retrieval and Editing

### Soundness
3

### Presentation
2

### Contribution
3
