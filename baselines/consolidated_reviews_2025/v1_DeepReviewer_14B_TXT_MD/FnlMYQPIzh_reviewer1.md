### Summary

This paper introduces ConvINT, a semi-structured framework for understanding user intentions in conversational AI, addressing limitations in existing rigid and unstructured approaches. ConvINT organizes intentions into four aspects—situation, emotion, action, and knowledge—and a Weakly-supervised Reinforced Generation (WeRG) method is proposed for efficient annotation. Experimental results demonstrate significant improvements in downstream tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel semi-structured intention framework (ConvINT) that organizes user intentions into four key aspects (situation, emotion, action, and knowledge), providing a more holistic and fine-grained understanding compared to rigid slot-value structures or unstructured representations.

2. The authors propose an efficient Weakly-supervised Reinforced Generation (WeRG) method that combines diverse annotation sources with a coarse-to-fine labeling strategy, enabling the model to generate high-quality ConvINT annotations at scale. 

3. The WeRG method is evaluated on two datasets (DuRecDial and ESConv) and compared with strong baselines, including direct prompting and chain-of-thought prompting with zero-shot and few-shot settings.

4. The paper is well-structured and clearly written, with a logical flow that guides the reader through the motivation, methodology, and experiments.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation behind the [KNOWLEDGE] component in the ConvINT framework is unclear. The authors should provide a more detailed explanation of its role and significance within the framework. Specifically, it's not evident how this component differs from simply extracting entities or topics from the conversation. The paper needs to clarify whether this 'knowledge' refers to external knowledge, contextual knowledge, or a combination, and how it contributes to a deeper understanding of user intent beyond what can be captured by the 'situation' or 'action' components.

2. The evaluation of the WeRG method relies heavily on automatic metrics (e.g., F1, BLEU, BERTScore) and a limited human evaluation involving only three student annotators assessing 50 conversations each. The inter-annotator agreement is not mentioned, which is crucial for assessing the reliability of the human evaluation. The sample size of 50 conversations might not be sufficient to generalize the findings, and the use of student annotators might introduce bias or lack of expertise in the domain. The paper should also consider including metrics that evaluate the quality of the generated annotations in terms of their impact on downstream tasks, rather than just surface-level similarity to reference annotations.

3. The authors could discuss potential biases in the datasets used (DuRecDial and ESConv) and how these biases might affect the generalizability of the WeRG method to other domains or types of conversations. For example, the datasets might contain specific cultural biases or be limited in the range of emotions or situations represented. The paper should also address potential biases introduced by the annotation process itself, especially given the use of weak supervision.

4. The paper could benefit from a more thorough discussion of the limitations of the proposed ConvINT framework and the WeRG method, including scenarios where they might not perform well or challenges in scaling to other languages or domains. For instance, the framework might struggle with implicit intentions or conversations where the user's goal is not clearly defined. The paper should also discuss the computational cost of the WeRG method and its scalability to larger datasets.

### Suggestions

The paper should provide a more rigorous justification for the [KNOWLEDGE] component within the ConvINT framework. It is essential to clarify whether this component captures external knowledge, contextual understanding, or both. The authors should provide concrete examples demonstrating how the [KNOWLEDGE] component adds value beyond what is captured by the [SITUATION] and [ACTION] components. For instance, if the conversation is about booking a flight, while the [SITUATION] might capture the intent to travel, and [ACTION] might capture the act of booking, the [KNOWLEDGE] component should clarify specific information like preferred airlines, seating arrangements, or loyalty programs. The authors should also discuss how this knowledge is represented and utilized by the model. A clear definition and examples will help to justify the necessity and utility of this component.

To strengthen the evaluation, the authors should expand the human evaluation by including a larger number of annotators with diverse backgrounds and expertise. The inter-annotator agreement should be reported using metrics like Cohen's Kappa or Fleiss' Kappa to ensure the reliability of the human evaluation. The evaluation should also include metrics that assess the impact of the generated annotations on downstream tasks, such as response quality or task completion rates. This would provide a more comprehensive understanding of the practical utility of the WeRG method. Furthermore, the authors should consider using more sophisticated evaluation metrics beyond surface-level similarity, such as metrics that evaluate the semantic quality and coherence of the generated annotations. The paper should also include an analysis of the types of errors made by the WeRG method and discuss potential strategies for addressing these errors.

The authors should also address potential biases in the datasets and the annotation process. A detailed analysis of the datasets should be included, discussing potential cultural biases, limitations in the range of emotions or situations represented, and any other biases that might affect the generalizability of the WeRG method. The paper should also discuss potential biases introduced by the weak supervision approach and how these biases might impact the generated annotations. The authors should also explore the performance of the WeRG method on datasets from different domains or languages to assess its robustness and generalizability. Finally, the paper should include a discussion of the computational cost of the WeRG method and its scalability to larger datasets, as well as the limitations of the framework in handling implicit intentions or conversations where the user's goal is not clearly defined.

### Questions

1. Could the authors provide more detailed explanations of the [KNOWLEDGE] component's role in the ConvINT framework and how it contributes to understanding user intentions?

2. What measures were taken to ensure the quality and consistency of the human-annotated data used in the WeRG method?

3. How do the authors plan to address the limitations of the ConvINT framework and the WeRG method in future work?

### Rating

6

### Confidence

4

**********
