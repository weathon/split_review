# Text-Augmented Multimodal LLMs for Chemical Reaction Condition Recommendation

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
High-throughput reaction condition (RC) screening is fundamental to chemical synthesis. However, current RC screening suffers from laborious and costly trial-and-error workflows. Traditional computer-aided synthesis planning (CASP) tools fail to find suitable RCs due to data sparsity and inadequate reaction representations. Nowadays, large language models (LLMs) are capable of tackling chemistry-related problems, such as molecule design, and chemical logic Q\&A tasks. However, LLMs have not yet achieved accurate predictions of chemical reaction conditions. Here, we present Chemma-RC, a text-augmented multimodal LLM that responds to task-specific questions by generating answers about reaction conditions. It learns a unified reaction representation via modality alignment from a corpus of reactions and question prompts, molecular structures in SMILES format, and graphical representations of chemical reactions.  We construct a 1.2 million pair-wised Q\&A instruction dataset to train Chemma-RC and design a projection module for modality alignment. Our experimental results demonstrate that Chemma-RC achieves state-of-the-art performance on two open benchmark datasets and exhibits strong generalization capabilities on out-of-domain (OOD) and High-Throughput Experimentation (HTE) datasets. Chemma-RC has the potential to accelerate high-throughput condition screening in chemical synthesis.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Chemma-RC, a multimodal large language model designed for recommending chemical reaction conditions. It integrates SMILES, reaction graphs, and textual descriptions to improve prediction accuracy, supported by a dataset of 1.2 million question-and-answer pairs. Experimental evaluations on benchmark datasets demonstrate its effectiveness in various contexts. The Perceiver module enhances alignment between data modalities, contributing to the model's strong performance.

### Strengths
Chemma-RC captures the complexity of chemical reactions more comprehensively by combining multiple modalities, including SMILES, graph structures, and textual corpora. This integration may enhance the model's understanding and predictive capabilities regarding reaction conditions. Chemma-RC is trained on a dataset of 1.2 million question-and-answer pairs, significantly enhancing the model's learning efficacy and accuracy, especially in high-throughput experiments. By incorporating text-augmented instruction prompts, Chemma-RC effectively guides the model in learning and generating reaction conditions.

### Weaknesses
Integrating multiple modalities enhances the model's abilities but also complicates it, potentially leading to longer training durations and increased debugging challenges.
The model depends on extensive, high-quality multimodal data for training, which may be difficult to obtain, particularly in data-scarce environments.
The complexity of the model can hinder its interpretability, making it challenging to trace the rationale behind specific predictions, a crucial aspect in chemistry.
The model's high complexity may result in overfitting, especially when training datasets are small or noisy.
Although effective with existing multimodal data, the model might struggle to adapt to new data types or domains without adequate training examples.
The model’s success is closely tied to the quality of its training data; poor or biased data can lead to inaccurate reaction condition predictions.
Developing and training such a sophisticated model may require significant computational power and time, which could be a challenge for some research groups.
The model's performance may differ across various chemical conditions or experimental contexts, restricting its overall transferability.

### Questions
In Section 4.4, the ablation study highlights performance variations across different data types (SMILES, Graph, Corpus). However, it would be helpful to specify how the model utilizes each modality to enhance predictions.
In Section 4.6, the term "top-1 partial match accuracy" in the results table requires clarification. The distinction between partial and complete matches, especially regarding reagent and solvent predictions, is not clearly defined.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper titled “Text-Augmented Multimodal Large Language Models for Chemical Reaction Condition Recommendation” introduces Chemma-RC, a novel multimodal large language model designed for chemical reaction condition recommendation (RCR). It leverages SMILES, reaction graphs, and textual corpus to improve the accuracy of RCR predictions and builds a 1.2 million pairwise Q&A dataset to train the model. Experimental results on USPTO benchmark datasets indicate that Chemma-RC achieves strong performance in both in-domain and out-of-domain settings, with a proposed Perceiver module for modality alignment.

### Strengths
1. Large-scale training data: Chemma-RC utilizes a dataset comprising 1.2 million pairs of question-and-answer instructions during training. The substantial size of this dataset may contribute to improved learning efficacy and accuracy of the model, enhancing its performance on high-throughput experimental data.

2. Generalization capability: The paper indicates that Chemma-RC performs well on out-of-domain (OOD) and high-throughput experimentation (HTE) datasets, demonstrating its robustness and adaptability across different data distributions.

### Weaknesses
1. While the paper presents Chemma-RC as a novel multimodal model, the experimental results lack sufficient evidence that its core techniques—such as modality alignment and instruction tuning—offer a distinct advantage over simpler models like T-Rex and TextReact. To address this, I recommend that the authors include specific comparisons to highlight the unique contributions of Chemma-RC. For example, broadening the set of baseline models beyond T-Rex and TextReact could provide a more comprehensive view of Chemma-RC’s competitive edge. The current analysis does not sufficiently demonstrate why the incorporation of textual information improves the model's accuracy, especially given that graph- or SMILES-based models often outperform even advanced text-only models.

2. While the manuscript addresses certain aspects of generalization (e.g., OOD and HTE results), it would benefit from additional evaluations to comprehensively demonstrate Chemma-RC’s versatility in chemical reaction modeling. For instance, models like TextReact illustrate their flexibility by performing multiple tasks, including reaction condition prediction and retrosynthesis. To parallel these capabilities, I suggest that the authors add experiments to assess Chemma-RC on diverse predictive tasks, such as reaction condition recommendation (RCR) using the USPTO dataset, as in TextReact. Additionally, it would be valuable to report how Chemma-RC performs under different dataset splits, such as random split (RS) and time split (TS), to further highlight its robustness across varied conditions.

3. The construction and training of Chemma-RC, as a complex multimodal model, may demand substantial computational resources and time, potentially creating challenges for research teams with limited access to high-performance computing. To make the model more accessible, I suggest the authors provide details on the computational requirements (e.g., training time, hardware specifications) and consider exploring ways to reduce these demands, such as model simplifications or alternative training strategies. This would offer clearer guidance for teams looking to replicate or adapt Chemma-RC within resource constraints.

4. While integrating multiple modalities indeed enhances the model's capabilities, it also increases its complexity, potentially leading to extended training times and additional debugging challenges. To assist others in implementing or building upon this work, I suggest that the authors discuss any specific challenges they encountered during the model’s training and debugging process due to its complexity. Insights into how these issues were addressed, including strategies or tools used to streamline debugging, would be valuable additions to the community and provide practical guidance for future work.

5. The model’s dependence on a large volume of high-quality multimodal data may limit its applicability in fields with limited data availability. I recommend that the authors discuss how Chemma-RC might perform with smaller datasets and explore potential strategies for adapting it to data-scarce domains. For example, they could consider approaches such as transfer learning, data augmentation, or semi-supervised learning to enhance the model's applicability where data is less abundant. Including these insights would make the model’s utility more broadly applicable to real-world scenarios.

6. Given the model's complexity, there is an inherent risk of overfitting, particularly in cases of limited or noisy training data. I suggest that the authors provide details on any regularization techniques or strategies they employed to mitigate overfitting. Additionally, discussing how they validated the model’s performance on unseen data—such as through cross-validation or using an independent test set—would help clarify the model’s robustness and reliability. These insights would be valuable for understanding the model's generalization capabilities in varied data environments.

### Questions
1. What are the results of the reaction condition recommendation (RCR) when using the USPTO dataset employed by the TextReact model, and how do the results differ when the dataset is partitioned according to RS (random split) and TS (time split)?

2. In Abstract: The term "unified reaction representation" might need clarification. It would be helpful to specify how the SMILES, reaction graphs, and textual corpus are integrated into this unified representation.

3. In Introduction (Lines 38-39): The problem of "low sparsity of chemical data" is mentioned but could be better explained. It’s unclear if this refers to limited diversity in reaction data or the low availability of high-quality reaction data.

4. Figure 1 - Model architecture description: The diagram of Chemma-RC's architecture (Figure 1) is complex, and the explanation in the text doesn’t fully clarify how each component (e.g., modality projection and condition prediction) interacts within the model. A step-by-step walkthrough could enhance understanding.

5. In section 3.2.1 - Text-Augmented Instruction Prompts: The description of how prompts are constructed might benefit from more examples, especially regarding "question templates" and their variety. It is unclear how "2,000 question templates" differ in structure or content and how these templates influence model training.

6. In section 4.3 - Performance Comparison (Tables 2 and 3): The term "strict matching policy" for top-k accuracy might need clarification. It’s unclear what criteria are used for strict matching—whether it’s an exact match of predicted and true labels or some other criteria.

7. Ablation Study (Section 4.4): While this section reports performance changes with various data types (SMILES, Graph, Corpus), it would be beneficial to clarify how the model interprets these individually. For example, what specific information from each modality improves the prediction?

8. In section 4.6 - Zero-Shot Prediction on High-Throughput Experimentation: The phrase "top-1 partial match accuracy" in the results table needs explanation. It is unclear what is considered a partial match versus a complete match, particularly for reagent and solvent prediction.

9. In Conclusion and Limitations: The paper mentions plans to "optimize data representation with full fine-tuning training strategies" but doesn’t clarify why full fine-tuning was not initially used. It would be helpful to understand the limitations of the current training strategy and how it impacts model performance.

10. In Appendix B - Data Description: In the dataset descriptions, some technical terms like "sparsity analysis" might be confusing. A brief explanation of "non-empty count" and "density" could aid in understanding the data distribution.

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
The authors present a novel Chemma-RC model designed for chemical reaction recommendation and prediction tasks. This model is trained on multiple data representations, including SMILES notations, reaction graphs, and chemical reaction recommendation corpora. Additionally, the authors introduce an instruction dataset comprising data from various sources, which has been augmented with textual templates. They further demonstrate that the Chemma-RC model can be easily fine-tuned on out-of-distribution data, enabling it to generalize to new types of chemical reactions.

### Strengths
The application of language models to chemical reaction planning represents a highly valuable direction for research. While the incorporation of additional data modalities into language models is not entirely novel, it is still an important approach that has the potential to enhance current methodologies by utilizing a broader range of available data. Moreover, the demonstrated ability of the Chemma-RC model to handle out-of-distribution data adds further significance to this work.  Experimental results and ablation study sections are comprehensive.

### Weaknesses
While the paper is generally well-written, certain sections lack clarity and sufficient justification for specific decisions made in the study. Additional details on these issues can be found in the Question section.

* What is the specific purpose of introducing the new dataset? Aside from integrating available data through templating, what novel contributions does this dataset offer? According to the paper, templates were generated using the GPT-4 model. How was the correctness of these generated templates verified?
* The purpose of using reaction graph embeddings remains unclear based on the current ablation study. Integrating graph embeddings requires additional effort including language model’s source code modification, yet Table 4 shows only a slight improvement in model performance with their usage. It appears that relying solely on textual corpora and SMILES representations might be sufficient. It may be beneficial to include an additional ablation study demonstrating cases where graph embeddings significantly enhance performance.
* One of the main contributions of the paper is the integration of multiple data representations and sources within a unified paradigm, positioning the proposed model closer to multi-task, multi-domain foundational models rather than single-task models, mainly presented in the Experimental section. To strengthen the significance of the results, it would be beneficial to include comparisons with current state-of-the-art chemical language models that address reaction planning tasks in their scopes, such as [a, b].

### Questions
* What is the specific purpose of introducing the new dataset? Aside from integrating available data through templating, what novel contributions does this dataset offer? According to the paper, templates were generated using the GPT-4 model. How was the correctness of these generated templates verified?
* The purpose of using reaction graph embeddings remains unclear based on the current ablation study. Integrating graph embeddings requires additional effort including language model’s source code modification, yet Table 4 shows only a slight improvement in model performance with their usage. It appears that relying solely on textual corpora and SMILES representations might be sufficient. It may be beneficial to include an additional ablation study demonstrating cases where graph embeddings significantly enhance performance.
* One of the main contributions of the paper is the integration of multiple data representations and sources within a unified paradigm, positioning the proposed model closer to multi-task, multi-domain foundational models rather than single-task models, mainly presented in the Experimental section. To strengthen the significance of the results, it would be beneficial to include comparisons with current state-of-the-art chemical language models that address reaction planning tasks in their scopes, such as [a, b].

a. BioT5+: Towards Generalized Biological Understanding with IUPAC Integration and Multi-task Tuning, 2024

b. nach0: multimodal natural and chemical languages foundation model, 2024

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on chemical reaction condition recommendation using LLMs. It proposes incorporating different data modalities, such as reaction formulas, graph-structured molecules, and reaction descriptions, into a single multimodal large language model (LLM) called Chemma-RC, fine-tuned through the Llama 2 model. The model is compared to previous baselines and shows promise in generating useful reaction conditions to accelerate high-throughput condition screening in chemical synthesis. Overall, the proposed method is interesting.

### Strengths
**Originality**: The paper focuses on an interesting problem with a reasonable solution. This is a useful and new case demonstrating the effectiveness of multimodal LLMs in drug discovery.

**Quality**: The proposed method seems promising.

**Clarity**: The paper includes figures to aid readability, with a well-illustrated method. The experimental setups and baselines are properly introduced.

**Significance**: The paper shows promising contributions to reaction condition recommendation.

### Weaknesses
1. Reaction condition recommendation is not a novel task in the era of LLMs. The paper needs a more thorough discussion and demonstration of why research focus should shift to LLM-based reaction condition recommendation. Do LLMs truly provide higher accuracy? Or do LLMs offer more interpretability through text generation? Has any work benchmarked the performance of LLMs in reaction condition recommendation?

2. Why are there two types of condition prediction modules mentioned in line 76? There is no motivation provided for them. LLMs are more naturally suited for generative tasks rather than prediction; why is prediction necessary here?

3. The ablation studies should be improved. In Table 4, consider adding a study that enables SMILES and graphs but disables the corpus (i.e., disabling the LLM part of the model).

4. There is a lack of detailed description regarding the process of constructing the question-answering dataset. Do the authors ensure that there is no data leakage? How was the data collected and deduplicated?

### Questions
1. In line 66: How can one determine that the LLMs are pre-trained on extensive reaction data?

2. Line 80: The term "Perceiver" appears without context. Please add a citation and provide an introduction.

3. In line 84/4.5: What distinguishes the USPTO 500MT Condition dataset from the USPTO-Condition dataset, and what causes their distributional differences? Are there any statistical results indicating that these tasks are out-of-distribution?

4. Figure 1 needs improvement. The boxes for data and model are indistinguishable, or there are no boxes, making it difficult for readers to determine where to begin.

5. Tables should be self-explanatory. In Table 1, what does the condition label mean?

6. In lines 300-303: Is there a specific reason why the authors freeze the parameters of all models and only fine-tune the projectors?

### Soundness
2

### Presentation
2

### Contribution
2
