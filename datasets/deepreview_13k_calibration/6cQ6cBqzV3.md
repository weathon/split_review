# LoRA-X: Bridging Foundation Models with Training-Free Cross-Model Adaptation

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 6, 3

## Abstract
The rising popularity of large foundation models has led to a heightened demand for parameter-efficient fine-tuning methods, such as Low-Rank Adaptation (LoRA), which offer performance comparable to full model fine-tuning while requiring only a few additional parameters tailored to the specific base model. When such base models are deprecated and replaced, all associated LoRA modules must be retrained, requiring access to either the original training data or a substantial amount of synthetic data that mirrors the original distribution. However, the original data is often inaccessible due to privacy or licensing issues, and generating synthetic data may be impractical and insufficiently representative. These factors complicate the fine-tuning process considerably. To address this challenge, we introduce a new adapter, Cross-Model Low-Rank Adaptation (LoRA-X), which enables the training-free transfer of LoRA parameters across source and target models, eliminating the need for original or synthetic training data. Our approach imposes the adapter to operate within the subspace of the source base model. This constraint is necessary because our prior knowledge of the target model is limited to its weights, and the criteria for ensuring the adapter’s transferability are restricted to the target base model’s weights and subspace.  To facilitate the transfer of LoRA parameters of the source model to a target model, we employ the adapter only in the layers of the target model that exhibit an acceptable level of subspace similarity. Our extensive experiments demonstrate the effectiveness of LoRA-X for text-to-image generation, including Stable Diffusion v1.5 and Stable Diffusion XL.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the challenges associated with the fine-tuning of large foundation models, particularly in the context of Low-Rank Adaptation (LoRA). It highlights the complications that arise when base models are deprecated, necessitating the retraining of LoRA modules without access to original training data due to privacy or licensing constraints. To mitigate these issues, the authors propose a novel adapter that facilitates the transfer of LoRA parameters between source and target models without requiring original or synthetic training data. The method operates within the subspace of the source model and focuses on layers of the target model that demonstrate sufficient subspace similarity. The effectiveness of the proposed method is validated through extensive experiments in text-to-image generation tasks.

### Strengths
1. The introduction of LoRA-X presents a significant advancement in parameter-efficient fine-tuning by enabling the transfer of LoRA parameters without the need for retraining, addressing a critical gap in the existing methodologies. The solution is highly relevant in real-world applications where access to original training data is often restricted, making it a valuable contribution to the field.
2. The paper includes extensive experiments demonstrating the effectiveness of LoRA-X across multiple models and tasks, providing strong empirical support for the proposed method.

### Weaknesses
1. The paper should discuss the scalability of LoRA-X for larger models or more complex tasks beyond text-to-image generation.
2. The reliance on subspace similarity may restrict the applicability of LoRA-X to models that are closely related, potentially limiting its use in more diverse model architectures.

### Questions
See the weaknesses for details.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the binding issue between LoRA models and their base models in data-scarce scenarios. It introduces Cross-Model Low-Rank Adaptation (LoRA-X), an adapter that operates within the subspace of pre-trained diffusion models to facilitate style transfer from the source base model to the target base model. Qualitative and quantitative experiments demonstrate its effectiveness.

### Strengths
1.  This is a meaningful work, addressing a common industry limitation: the need to retrain LoRA when changing the pre-trained model. 

2. The paper introduces a subspace perspective for Stable Diffusion models, which may inspire future research.

### Weaknesses
1. The paper lacks comparisons with recent works, such as [1].

2. It is better to conduct some visualization to illustrate the motivation. This may better show the effects of the same LoRA model combined with different base models to highlight this pressing challenge.

3. The experiments appear overly simplistic:

(1)  There is no baseline; for models based on SD 1.5, SD 1.5 should serve as the baseline, and the same applies to SDXL.

(2)  In Section 5.2, there is a lack of quantitative analysis for the target model without LoRA-X and for [1]. Additionally, the source row seems redundant and could be placed in later experiments, as the main experiment only needs to compare different methods.

(3)  In Section 5.3, at least two to three datasets are needed to compare the performance drop of the LoRA-X style transfer method against LoRA. Furthermore, the ranks of LoRA-X and LoRA are not the same; comparisons under the same rank are missing.

(4)  There is no experiment on the impact of rank on LoRA-X performance.

(5)  In all tables, "Results in Green and Red show less than and more than 10% difference" should be replaced with ± percentage for clarity.

4. The writing details need further refinement, as noted in the Questions, to avoid reader confusion.

### Questions
Q1: The term "base model" is unclear in the paper. If the source model is SD 1.5, does the target model refer to the pre-trained model fine-tuned based on SD 1.5 or SD XL? Although the experiments indicate that the latter is challenging and lack corresponding quantitative analysis, this should be clarified in the introduction, specifying that it refers to the former.

Q2: In Figure 2, the phrase "without access to the original data" in the introduction suggests that the target model (b) does not require training, but the source model (a) still needs data. Similar to Q1, the semantics should be clarified in the text.

Q3: In Section 4.2.2, the phrase "linear transformation can be evaluated as P" raises questions about the relationship between P and the subsequent formula U_s . Why is P mentioned?

Q4: In Section 5.3, the statement "We repeated the experiment for different LoRA ranks to show how LoRA’s transferability drops as rank is reduced, though its total size remains much higher than LoRA-X" needs clarification on which specific metric in Table 2 illustrates this transferability.

Q5: In Section 5.4.2, the \Delta \Sigma_s row is not represented in Table 4.

### Soundness
3

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
3

### Summary
This study introduces LoRA-X to address the transferability problem of existing PEFT techniques across base models. It enables training-free cross-model adaptation by constraining the adapter within the source model’s subspace. LoRA-X demonstrates effective performance on text-to-image tasks, allowing seamless transfer without requiring original or synthetic data for retraining.

### Strengths
1. The introduction of LoRA-X as a training-free cross-model adapter addresses a significant limitation in PEFT. It allows adapters to be used across different base models without retraining or data access.

2. LoRA-X maintains a low parameter footprint, which is essential for computational efficiency.

### Weaknesses
1. The study only focuses on text-to-image tasks, which limits its applications to other domains such as NLP or time-series data.

2. LoRA-X has higher transfer costs when applied across significantly different architectures.

3. LoRA-X is only compared with the traditional LoRA. This could be strengthened by comparing LoRA-X's training-free transfer method with other recent PEFT techniques or knowledge distillation methods

### Questions
1. How well does LoRA-X perform across other types of tasks or domains, like NLP or time-series analysis? Would additional fine-tuning be needed to adapt it effectively?

2. How does LoRA-X perform relative to techniques like Trans-LoRA or SVDiff in terms of computational efficiency and performance? Could a direct comparison be provided?

3. Does the complexity of the transfer process increase significantly with larger models, and what optimizations could make it more scalable?

4. Is there a recommended threshold for subspace similarity that ensures effective transfer without sacrificing performance? How sensitive is LoRA-X to variations in this threshold?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper titled "LoRA-X: Bridging Foundation Models with Training-Free Cross-Model Adaptation" introduces a novel adapter, LoRA-X (Cross-Model Low-Rank Adaptation), which enables the transfer of fine-tuning parameters across different base models without the need for additional training or access to original training data. This is particularly useful when base models are updated or replaced, and retraining adapters is required.

### Strengths
1. The work presents LoRA-X, an innovative adapter that enables training-free parameter-efficient transfer across different base models. This approach holds significance in addressing the migration of adapters when base models are updated or replaced, especially considering scenarios where data privacy and licensing issues prevent access to original training data.
2. In introducing the LoRA-X method, the paper provides a solid theoretical analysis and experimental validation. The theoretical part establishes a strong foundation for the design of LoRA-X by comparing the expressiveness of different PEFT (Parameter-Efficient Fine-Tuning) methods. The experimental part verifies the effectiveness of LoRA-X in text-to-image generation tasks, including style transfer and knowledge distillation scenarios. These results support the potential of your method in practical applications. Additionally, the paper offers a detailed analysis of the LoRA-X transfer process, including subspace similarity metrics, which add depth and persuasiveness to the paper.
3. The structure of the paper is clear, and the logic is coherent. From the introduction to related work, and then to the detailed introduction of LoRA-X and experimental results, each part is closely connected and easy to understand.

### Weaknesses
1. The paper's comparison of LoRA-X with other parameter-efficient fine-tuning methods is not comprehensive enough. I suggest the authors enhance the comparative analysis with existing methods, particularly the latest ones, to highlight the advantages of LoRA-X and potential areas for improvement. Specifically, the paper lacks a detailed comparison with methods that also explore weight decomposition or frequency-based adaptation, which could provide a more nuanced understanding of LoRA-X's performance relative to the state-of-the-art.
2. The paper introduces the cross-model adapter LoRA-X but does not emphasize which specific task the method focuses on. While the experimental section shows excellent performance in text-to-image generation tasks, its potential application in other domains is not fully explored. If the method is limited to a particular task, it would be beneficial to clarify this at the beginning of the paper to help readers understand better. Alternatively, if LoRA-X can be applied to multiple different application areas and tasks, a thorough discussion of its performance across various tasks would be valuable. The current presentation leaves ambiguity regarding the generalizability of the proposed method.
3. The paper's description of the implementation details of LoRA-X, including the specific implementation and optimization strategies of the algorithm, is not detailed enough. I recommend the authors provide more implementation details, including pseudocode or flowcharts of the algorithm, as well as any specific optimization measures taken. The lack of clarity in implementation details makes it difficult to reproduce the results and assess the practical applicability of the method. For example, specific choices of optimizers, learning rate schedules, and initialization strategies are not clearly stated.

### Questions
1. The third section of the paper devotes an entire section to discussing the motivation, clearly explaining the relevant content. However, it is debatable whether such an extensive section is necessary to elaborate on the motivation.
2. There appears to be a significant formatting issue at the bottom of page 3 and the top of page 4.

### Soundness
2

### Presentation
2

### Contribution
2
